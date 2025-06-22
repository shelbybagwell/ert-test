import logo from './logo.svg';
import './App.css';
import { getData } from './Api';
import { useState } from 'react';

function App() {
  const [data, setData] = useState(null);
  
  return (
    <div className="App">
      <header className="App-header">
        <p>test</p>
        <DataButton onSuccess={setData} />
        {Array.isArray(data) ? (
        <DataTable rows={data} />
      ) : data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : null}
      </header>
    </div>
  );
}

function DataButton({ onSuccess }) {
  const handleClick = async () => {
     try {
      const result = await getData("/rtsw?persist=true");
      onSuccess(result);
      console.log(result);
    }
    catch {
      console.error("GET request failed, could not get RTSW data.");
    }
  }
  return (
    <button onClick={handleClick}>Get RTSW Data</button>
  )
}

function DataTable({ rows }) {
  if (!rows || rows.length == 0) {
    return <p>No data yet</p>;
  }
  const headers = Object.keys(rows[0]);

  return (
    <table border="1" cellPadding="8">
      <thead>
        <tr>
          {headers.map((key) => (
            <th key={key}>{key}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {rows.map((row, i) => (
          <tr key={i}>
            {headers.map((key) => (
              <td key={key}>{row[key]}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default App;
