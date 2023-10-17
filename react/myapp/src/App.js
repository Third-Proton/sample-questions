import React from 'react';
import './App.css';

/**
 *
 * For this example:
 *
 * 1. In general, describe React state and references, and any differences / similarities / use cases for each.
 * 2. Describe what the 'useEffect' hook is doing in this example.
 * 3. Describe what happens when you click on each of the three paragraphs (p1, p2, p3) in the sample below.
 * 4. Describe what each paragraph (including the 'data' paragraph) will show after clicking on p1, p2, and p3.
 *
 */

function App() {
  const [clickCount, setClickCount] = React.useState(0);
  const clickCountRef = React.useRef(0);
  const [appData, setAppData] = React.useState({});

  const p1Click = (e) => {
    setClickCount(clickCount + 1);
  };

  const p2Click = (e) => {
    clickCountRef.current = clickCountRef.current + 1;
  };

  const p3Click = (e) => {
    e.preventDefault();

    setClickCount(clickCount + 1);
    clickCountRef.current = clickCountRef.current + 1;
  };

  React.useEffect(() => {
    setAppData(data => {
      data.clickCount = clickCount;
      data.clickCountRef = clickCountRef.current;
      return data;
    });
  }, [clickCount]);

  return (
    <div className="App">
      <header className="App-header">
        <p id='p1' onClick={p1Click}>Click me ({clickCount})</p>

        <p id='p2' onClick={p2Click}>Click me ({clickCountRef.current})</p>

        <p id='p3' onClick={p3Click}>Click me ({clickCount} + {clickCountRef.current})</p>

        <p id='data'>{JSON.stringify(appData)}</p>
      </header>
    </div>
  );
}

export default App;
