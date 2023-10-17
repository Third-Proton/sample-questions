import React from 'react';
import './App.css';

function App() {
  const [clickCount, setClickCount] = React.useState(0);
  const clickCountRef = React.useRef(0);

  const p1Click = (e) => {
    setClickCount(clickCount + 1);
  };

  const p2Click = (e) => {
    clickCountRef.current = clickCountRef.current + 1;
  };

  const p3Click = (e) => {
    clickCountRef.current = clickCountRef.current + 1;
    setClickCount(clickCount + 1);
  };

  return (
    <div className="App">
      <header className="App-header">
        <p id='p1' onClick={p1Click}>Click me ({clickCount})</p>
        <p id='p2' onClick={p2Click}>Click me ({clickCountRef.current})</p>
        <p id='p3' onClick={p3Click}>Click me ({clickCount} + {clickCountRef.current})</p>
      </header>
    </div>
  );
}

export default App;
