
function save() {
  // Get the data from the HTML side
  var name = document.getElementById("user-name").value;
  var surname = document.getElementById("user-surname").value;

  fetch("http://localhost:8080/", {
    method: 'POST',
    body: JSON.stringify({
      "name": name,
      "surname": surname
    })
  }).then(async (response) => {
    var user = await response.json()
    printResults(user)
  }).catch((err) => {
    console.error(err);
  })
}

function printResults(user) {
  document.getElementById("result-holder").innerHTML = user.id;
}

function getUsers() {
  fetch("http://localhost:8080/", {
    method: 'GET'
  }).then(async (response) => {
    var users = await response.json()
    printUsers(users)
  }).catch((err) => {
    console.error(err);
  })
}

// `users` is an array of arrays.
function printUsers(users) {
  const tableBody = document.getElementById("user-data");

  for (let index = 0; index < users.length; index++) {
    const user = users[index];
    var id = user[0];
    var name = user[1];
    var surname = user[2];
    
    // Expected end result (example):
    // <tr>
    //   <td>1</td>
    //   <td>Luyanda</td>
    //   <td>Zulu</td>
    // </tr>
    var tr = document.createElement("tr");

    // This is the ID cell
    var idTd = document.createElement("td");
    idTd.innerHTML = id;

    // This is the Name cell
    var nameTd = document.createElement("td");
    nameTd.innerHTML = name;

    // This is the Surname cell
    var surnameTd = document.createElement("td");
    surnameTd.innerHTML = surname;

    // Append all the cells to the row
    tr.append(idTd, nameTd, surnameTd);

    tableBody.append(tr);
  }
}