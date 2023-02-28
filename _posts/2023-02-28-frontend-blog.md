---
toc: true
description: What has been done in the frontend
categories: [T2, post]
title: Frontend Blog
author: Evan Aparri
show_tags: true
comments: true
---
## Inputs
```
        <!-- Game Over -->
        <div id="gameover" class="py-4 text-light">
            <p>Game Over, press the <span style="background-color: #d4ca1c; color: #000000">New Game</span> button to play again</p>
            <p><span style="background-color: #FFFFFF; color: #000000">Your username must have exactly 3 characters in order to log your score.</span></p>
            <form action="javascript:create_user()">
                <p><label>
                    Username for Player 1:
                    <input type="text" name="user1" id="user1" placeholder="Must have 3 characters" required>
                </label></p>
                <p><label>
                    Username for Player 2:
                    <input type="text" name="user2" id="user2" placeholder="Must have 3 characters" required>
                </label></p>
                <p><label>
                    Score for Player 1:
                    <span name="scoring_1" id="scoring_1">0</span>
                </label></p>
                <p><label>
                    Score for Player 2:
                    <span name="scoring_2" id="scoring_2">0</span>
                </label></p>
                <p><label>
                    Player 1: 
                    <span name="gameResult1" id="gameResult1">Result is displayed here.</span>
                </label></p>
                <p><label>
                    Player 2: 
                    <span name="gameResult2" id="gameResult2">Result is displayed here.</span>
                </label></p>
                <!-- <p><label>
                    Date of Score:
                    <span type="date" name="dos" id="dos"></span>
                </label></p> -->
                <p>
                    <button id="post" onclick="alert('Your score has been posted!')">Submit</button>
                </p>
            </form>
            <!-- <a id="new_game1" class="link-alert">new game</a>
            <a id="setting_menu1" class="link-alert">settings</a> -->
        </div>
```
The users can put in a username, but the api ensures that the number of characters used is three
The score is synnced with the game so the they can't be manually changed, same with the results of the game.
The date ends up being automatically added without needed input after the POST method is used.

## Create
```
  // prepare URL's to allow easy switch from deployment and localhost
  //const url = "http://127.0.0.1:8086/api/pong"
  const url = "https://pythonalflask.tk/api/pong"
  const create_fetch = url + '/addPongScore';
  // Load games on page entry
  function create_user(){
    // Creating json for the game
    const body = {
        user1: document.getElementById("user1").value,
        user2: document.getElementById("user2").value,
        score1: document.getElementById("scoring_1").innerHTML,
        score2: document.getElementById("scoring_2").innerHTML,
        result1: document.getElementById("gameResult1").innerHTML,
        result2: document.getElementById("gameResult2").innerHTML        

    };
    //using the POST method
    const requestOptions = {
        method: 'POST',
        body: JSON.stringify(body),
        mode: 'cors',
        cache: 'default',
        //credentials: 'include',
        headers: {
            "content-type": "application/json",
            'Authorization': 'Bearer my-token',
        },
    };
    // URL for Create API
    // Fetch API call to the database to create a new game
    fetch(create_fetch, requestOptions)
      .then(response => {
        // trap error response from Web API
        if (response.status !== 200) {
          const errorMsg = 'Database create error: ' + response.status;
          console.log(errorMsg);
          return;
        }
        // response contains valid result
        response.json().then(data => {
            console.log(data);
        })
    })
    // show refresh button
    PONG_REFRESH.style.display= "block";
    PONG_GAMEOVER.style.display= "none";
  }
```
This code helps fetch the API from the deployed flask server and creates the game after inputting information into the form (user1, user2).

## Read
```
  // Display Game history Table, data is fetched from Backend Database
  function read_users() {
    // prepare fetch options
    const read_options = {
      method: 'GET', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'default', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'omit', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
      },
    };

    // fetch the data from API
    fetch(read_fetch, read_options)
      // response is a RESTful "promise" on any successful fetch
      .then(response => {
        // check for response errors
        if (response.status !== 200) {
          const errorMsg = 'Database read error: ' + response.status;
          console.log(errorMsg);
          const tr = document.createElement("tr");
          const td = document.createElement("td");
          td.innerHTML = errorMsg;
          tr.appendChild(td);
          resultContainer.appendChild(tr);
          return;
        }
        // valid response will have json data
        response.json().then(data => {
          console.log(data);
          data.sort(function(a, b) {
            return new Date(b.scoreDate) - new Date(a.scoreDate);
          });
          for (let i = 0; i < data.length; i++) {
            const row = data[i];
            console.log(row);
            add_row(row);
          }
        })
      })
      // catch fetch errors (ie ACCESS to server blocked)
      .catch(err => {
        console.error(err);
        const tr = document.createElement("tr");
        const td = document.createElement("td");
        td.innerHTML = err;
        tr.appendChild(td);
        resultContainer.appendChild(tr);
      });
  }


  function add_row(data) {
    const tr = document.createElement("tr");
    const user1 = document.createElement("td");
    const user2 = document.createElement("td");
    const score1 = document.createElement("td");
    const score2 = document.createElement("td");
    const result1 = document.createElement("td");
    const result2 = document.createElement("td");
    const scoreDate = document.createElement("td");

  
    // obtain data that is specific to the API
    user1.innerHTML = data.user1; 
    user2.innerHTML = data.user2; 
    score1.innerHTML = data.score1;
    score2.innerHTML = data.score2;
    result1.innerHTML = data.result1;
    result2.innerHTML = data.result2;
    scoreDate.innerHTML = data.scoreDate;

    // add HTML to container
    tr.appendChild(user1);
    tr.appendChild(user2);
    tr.appendChild(score1);
    tr.appendChild(score2);
    tr.appendChild(result1);
    tr.appendChild(result2);
    tr.appendChild(scoreDate);

    resultContainer.appendChild(tr);
  }
```
This code fetches the API from the deployed server and displays the data in a table. The data displayed is sorted from the most recent to the oldest, all games are shown, but the search bar can limit the number of rows shown.