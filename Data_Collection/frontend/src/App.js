import './App.css';
import { getData } from './Api';
import { useState } from 'react';

function App() {
  const [data, setData] = useState(null);
  const [warning, setWarning] = useState(false);
  
  return (
    <div className="App">
      <header className="App-header">
        <h1>Solar Storm Early Warning</h1>
        
      </header>
      <div className='body'>
        <div className='left'>
        <DataButton onSuccess={setData} />
        <DataPopulated hasData={data} hasWarning={warning} />
      </div>
      <div className='right'>
        {Array.isArray(data) ? (
        <DataTable rows={data} warning={setWarning} />
      ) : data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : null}
      </div>
      </div>
    </div>
    
  );
}

function DataPopulated({ hasData, hasWarning }) {
  if (hasData) {
    if (hasWarning) {
    return (
      <p className='warningText'>Some values exceed threshold. Possible solar storm.</p>
    );
  }
  return (
    <p className='normalText'>No solar storms indicated.</p>
  );
  }
  return (
    <p className='normalText'>No data. Click button to populate table.</p>
  )
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
    <button className="rtswButton" onClick={handleClick}>Get RTSW Data</button>
  )
}

function DataTable({ rows, warning }) {
  if (!rows || rows.length === 0) {
    return <p>No data yet</p>;
  }
  const headers = Object.keys(rows[0]);
  const speedThreshold = 500;
  const densityThreshold = 10;

  return (
   <div className="table-container">
      <table className="responsive-table">
        <thead>
          <tr>
            {headers.map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>
       <tbody>
          {rows.map((row, i) => {
            const highlight =
              (row.speed !== undefined && row.speed > speedThreshold) ||
              (row.density !== undefined && row.density > densityThreshold);
              if (highlight) warning(true);
            return (
              <tr key={i} className={highlight ? "highlight" : ""}>
                {headers.map((key) => (
                  <td key={key}>{row[key]}</td>
                ))}
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default App;
