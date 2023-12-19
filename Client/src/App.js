import "./App.css";
import { useState } from "react";
import Api from "./Api.js";

function App() {
  const [result, setResult] = useState();
  const [value, setValue] = useState();
  const [apiResult, setApiResult] = useState();

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

  // const getKanbanCardByPhaseId = (id) => {
  //   const response = fetch(`http://127.0.0.1:5000/kanbancard/phase/${id}`, {
  //     method: "GET",
  //     headers: {
  //       Accept: "application/json, text/plain",
  //       "Content-type": "application/json",
  //     },
  //   }).then((res) => {
  //     return res.json();
  //   });
  //   setApiResult(response);
  //   console.log(response);
  // };

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
