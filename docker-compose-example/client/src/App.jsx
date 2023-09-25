import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom";

import "./index.css";

const App = () => {

  const[data,setData]=useState(null);

  const get=async()=>{
    const res=await fetch('http://127.0.0.1:8000')
    const data=await res.json()
    console.log(data.name)
    setData(data.name)
  }

  useEffect(()=>{
    get();
  },[])

  return (
    <>
      {
        data? <center><h3>{data}</h3></center>: <center><h3>Loading...</h3></center>
      }
    </>
  )
}
ReactDOM.render(<App />, document.getElementById("app"));
