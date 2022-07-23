
// const express = require("express");
// const bodyParser = require("body-parser");
// const ejs = require("ejs");
// const _ = require("lodash");
// // const { MongoClient } = require('mongodb');
// // const client = new MongoClient('mongodb://127.0.0.1:27017');

// // const app = express();
// // app.set('view engine', 'ejs');
// // app.use(bodyParser.urlencoded({extended: true}));
// // app.use(express.static("public"));
// // "mongodb://0.0.0.0:27017/";
// var url = "mongodb+srv://haneya20yo:20180221404@cluster0.aehspdr.mongodb.net/?retryWrites=true&w=majority";

// // create a client to mongodb
// var MongoClient = require('mongodb').MongoClient;
 
// // make client connect to mongo service
// MongoClient.connect(url, function(err, db) {
//     if (err) throw err;
//     // db pointing to newdb
//     console.log("Switched to "+db.databaseName+" database");
 
//     // document to be inserted

//     // insert document to 'users' collection using insertOne
//     // db.collection("blog").insertOne(doc);
// });

const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://haneya20yo:20180221404@cluster0.aehspdr.mongodb.net/?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 });
client.connect(err => {
    const collection = client.db("test").collection("devices");
    var doc = { name: "saman", age: "12" };
    // perform actions on the collection object
    collection.insertOne(doc);
//   client.close();
});
