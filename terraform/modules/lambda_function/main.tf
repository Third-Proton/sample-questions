##################################################################################
# RESOURCES
##################################################################################
resource "aws_cloudwatch_log_group" "logs" {
  name = "/aws/lambda/${var.function_name}"
  retention_in_days = 90
}

resource "aws_lambda_function" "function" {
  function_name = var.function_name
  role = var.iam_role
  filename = var.filename
  source_code_hash = filebase64sha256(var.filename)
  handler = var.handler
  memory_size = var.memory_size
  runtime = var.runtime
  timeout = var.timeout
  tracing_config {
    mode = "Active"
  }
  environment {
    variables = var.env_vars
  }
}

# Scheduled lambda resources (optional)
resource "aws_cloudwatch_event_rule" "scheduled_event" {
  count = length(var.schedule_expression) > 0 ? 1 : 0

  name = "${aws_lambda_function.function.function_name}-schedule"
  schedule_expression = var.schedule_expression
}

resource "aws_cloudwatch_event_target" "scheduled_event_target" {
  count = length(var.schedule_expression) > 0 ? 1 : 0

  rule  = aws_cloudwatch_event_rule.scheduled_event[0].name
  arn   = aws_lambda_function.function.arn
}

resource "aws_lambda_permission" "lambda_scheduled_event_permission" {
  count = length(var.schedule_expression) > 0 ? 1 : 0

  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.function.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.scheduled_event[0].arn
}
