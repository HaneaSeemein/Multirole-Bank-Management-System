
const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const _ = require("lodash");
const multer = require("multer");
const util = require("util");
const { MongoClient } = require('mongodb');
require('dotenv').config();
const { GridFsStorage } = require("multer-gridfs-storage");

const app = express();
const client = new MongoClient(process.env.databaseLink);
const imagestorageengine = multer.diskStorage({
  destination:(request,file,callback) => callback(null,'mongodb+srv://haneya20yo:20180221404@cluster0.aehspdr.mongodb.net/?retryWrites=true&w=majority'),filename:(request,file,callback) => callback(null,Date.now()+'_'+file.originalname)
})
var storage = new GridFsStorage({
  url: 'mongodb+srv://haneya20yo:20180221404@cluster0.aehspdr.mongodb.net/?retryWrites=true&w=majority/blog',
  options: { useNewUrlParser: true, useUnifiedTopology: true },
  file: (req, file) => `${Date.now()}--${file.originalname}`
});
const upload = multer({storage:imagestorageengine});
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

const homeStartingContent = "Lacus vel facilisis volutpat est velit egestas dui id ornare. Semper auctor neque vitae tempus quam. Sit amet cursus sit amet dictum sit amet justo. Viverra tellus in hac habitasse. Imperdiet proin fermentum leo vel orci porta. Donec ultrices tincidunt arcu non sodales neque sodales ut. Mattis molestie a iaculis at erat pellentesque adipiscing. Magnis dis parturient montes nascetur ridiculus mus mauris vitae ultricies. Adipiscing elit ut aliquam purus sit amet luctus venenatis lectus. Ultrices vitae auctor eu augue ut lectus arcu bibendum at. Odio euismod lacinia at quis risus sed vulputate odio ut. Cursus mattis molestie a iaculis at erat pellentesque adipiscing.";
const aboutContent = "Hac habitasse platea dictumst vestibulum rhoncus est pellentesque. Dictumst vestibulum rhoncus est pellentesque elit ullamcorper. Non diam phasellus vestibulum lorem sed. Platea dictumst quisque sagittis purus sit. Egestas sed sed risus pretium quam vulputate dignissim suspendisse. Mauris in aliquam sem fringilla. Semper risus in hendrerit gravida rutrum quisque non tellus orci. Amet massa vitae tortor condimentum lacinia quis vel eros. Enim ut tellus elementum sagittis vitae. Mauris ultrices eros in cursus turpis massa tincidunt dui.";
const contactContent = "Scelerisque eleifend donec pretium vulputate sapien. Rhoncus urna neque viverra justo nec ultrices. Arcu dui vivamus arcu felis bibendum. Consectetur adipiscing elit duis tristique. Risus viverra adipiscing at in tellus integer feugiat. Sapien nec sagittis aliquam malesuada bibendum arcu vitae. Consequat interdum varius sit amet mattis. Iaculis nunc sed augue lacus. Interdum posuere lorem ipsum dolor sit amet consectetur adipiscing elit. Pulvinar elementum integer enim neque. Ultrices gravida dictum fusce ut placerat orci nulla. Mauris in aliquam sem fringilla ut morbi tincidunt. Tortor posuere ac ut consequat semper viverra nam libero.";
// let allblogs = [];

// async function main() {
client.connect(()=>{
  const db = client.db('blog');
  console.log('Connected successfully to server')
  blogs = db.collection('blogs');
  users = db.collection('users');
  images = db.collection('images');
  var titles = [];
  var contents = [];
  var images = [];

  blogs.find().forEach(function(post){
    titles.push(post.title);
    contents.push(post.content);
    images.push(post.picture);
  })

  app.get("/", function(req, res){
    res.render("home", {
      startingContent: homeStartingContent,
      title: titles,
      content: contents,
      picture: images
    });
  });

  app.get("/about", function(req, res){
    res.render("about", {aboutContent: aboutContent});
  });

  app.get("/contact", function(req, res){
    res.render("contact", {contactContent: contactContent});
  });

  app.get("/compose",function(req, res){
    res.render("compose");
  });

  app.post("/compose", upload.single("postPicture"), function(req, res){
    blogs.insertOne({
      title: req.body.postTitle,
      content: req.body.postBody,
      picture: req.body.postPicture
    });
    titles.push(req.body.postTitle);
    contents.push(req.body.postBody);
    images.push(req.body.postPicture);
    console.log(req.file);
    res.redirect("/");
});

app.get("/posts/:postName", function(req, res){
  const requestedTitle = _.lowerCase(req.params.postName);
  titles.forEach(function(post){
    const storedTitle = _.lowerCase(post);
    if (storedTitle === requestedTitle) {
      blogs.find({"title":post}).forEach(function(conten){
        res.render("post", {
          title: post,
          content: conten.content
        })
      });
    }
  });
});

app.listen(3000, function() {
    console.log("Server started on port 3000");
  });
  return 'done.';
});
// main().then(server()).catch(console.error)
// .finally(()=>client.close());
// function server(){console.log("then");}
// .substring(0, 100) + " ..."


// <%   %>