import React, { useState, useEffect } from "react";

import logo from "./logo.svg";
import "./App.css";

const CALL_DELAY = 500;

function App() {
  const [ loading, setLoading ] = useState(true);
  const [ errorMessage, setErrorMessage ] = useState(null);
  const [ rows, setRows ] = useState({});

  useEffect(() => {
      let timer = setTimeout(() => {
        setLoading(true);
        fetch("/info")
          .then((resp) => {
            const status = resp.status;
            if(status === 200){
              console.debug(resp);
              setErrorMessage(null);
              return resp.json();
            }
            throw new Error(`Request failed with status ${status}`);
          })
          .catch((error) => {
            setErrorMessage(error.message);
            setLoading(false);
          })
          .then((data) => {
            const pids = { ...rows[data.hostname] };
            console.debug(pids);
            setRows({
              ...rows,
              [data.hostname]: {
                ...pids,
                [data.pid]: data.called,
              },
            });
            setLoading(false);
          });
      }, CALL_DELAY);

      return () => {
        clearTimeout(timer);
      };
  }, [loading, rows]);

  const error = errorMessage ? (
    <div>
      <b style={{ color: "red" }}>
        {errorMessage}
      </b>
    </div>
  ) : null;

  const renderedRows = Object.keys(rows).map((hostname) => {
    const row = rows[hostname];
    const totalCalled = Object.keys(row).reduce((prev, currPid) => {
      return prev + row[currPid];
    }, 0);

    return (
      <tr key={hostname}>
        <td>
          {hostname}
        </td>
        <td>
          {totalCalled}
        </td>
      </tr>
    )
  })


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h2> Server Calls </h2>
        <table>
            <thead>
              <tr>
                <th>
                  Hostname
                </th>
                <th>
                  Called
                </th>
              </tr>
            </thead>
            <tbody>
              {renderedRows}
            </tbody>
        </table>
        {error}
      </header>
    </div>
  );
}

export default App;
