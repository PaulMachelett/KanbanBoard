import "./App.css";
import { useState } from "react";
import Api from "./Api.js";

function App() {
  const [result, setResult] = useState();
  const [value, setValue] = useState();

  function countAndChangeState() {
    const resultValue = count(value);
    setResult(resultValue);
  }

  const handleInputChange = (e) => {
    setValue(e.target.value);
  };

  function count(number) {
    return 2 * number;
  }

  return (
    <div className="App">
      number:
      <input type="text" onChange={handleInputChange} />
      <button onClick={countAndChangeState}>Press me to calculate</button>
      <textarea value={result} readOnly></textarea>
      <Api />
    </div>
  );
}

export default App;
