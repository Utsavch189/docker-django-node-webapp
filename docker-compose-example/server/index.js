const express=require("express");

const cors = require('cors')

const app=express()
app.use(cors())

app.get("/",(req,res)=>{
          const ress={
                    "name":"utsav chatterjee"
          }
          res.json(ress)
})

app.listen(8000,()=>{
          console.log("running..")
})