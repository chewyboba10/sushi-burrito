---
toc: true
layout: post
description: Here is information on our team's project progress and what each member has been doing
categories: [T1, post]
title: Project Video and Transcript
author: Evan Aparri
show_tags: true
comments: true
---

# Project Video

<style>
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

.content {
  padding: 0 18px;
  display: none;
  overflow: hidden;
  background-color: #f1f1f1;
}
</style>

<h2>Collapsibles</h2>

<p>A Collapsible:</p>
<button type="button">Open Collapsible</button>
<div>
  <p>
  Hi my name is Evan Aparri and I am the DevOps of Frost. This week I changed the nginx configuration file to add PUT in places specified by Mr. Mortenson on Slack. (SWITCH TO NGINX FILE) PUT requests allow us to create resources in our project. For example, our Backend Developer, Alex, can make it so we could use PUT to create new accounts in order to keep track of our game's attempts done by different people. Alex has found a different way to do create users, and their info can be viewed using GET in our website(SWITCH TO API), but this user creation is not without its problems, which will be shown by our Frontend Developer, Haseeb. (SWITCH TO VSCODE)But as you can see, he has been making much progress in the creation of the API for users and score tracking in our flask repository. Alex will be going into more detail in the API later in the video. Our Scrum Master will now show us what our project is and its purpose.
  

  </p>
</div>

<style>
    body {
  padding: 20px;
  font-family: open sans, arial, helvetica;
  color: #333;
  background-color: lightblue;
}
.plus-minus:after,
.plus-minus.collapsed:after {
  display: inline-block;
  width: 1em;
  font-family: arial;
  font-weight: bold;
  text-align: center;
  position: relative;
}
.plus-minus:after {
  content:"-";
  top: -1px;
}
.plus-minus.collapsed:after {
  content:"+";
  top: 0;
}
</style>

<div>
<a class="btn btn-primary plus-minus" data-toggle="collapse" href="#collapseExample1" aria-expanded="true" aria-controls="collapseExample1">
  Link with href
</a> 

<div class="collapse in" id="collapseExample1">
me
</div>
<br/>
<button class="btn btn-primary plus-minus collapsed" type="button" data-toggle="collapse" data-target="#collapseExample2" aria-expanded="false" aria-controls="collapseExample2">
  Button with data-target
</button>
<div class="collapse" id="collapseExample2">
  me2
</div>


<br/>
<span class="btn btn-primary plus-minus collapsed" type="button" data-toggle="collapse" data-target="#collapseExample3" aria-expanded="false" aria-controls="collapseExample3">
  Button with data-target
</span>
<div class="collapse" id="collapseExample3">
  me3
</div>
</div>