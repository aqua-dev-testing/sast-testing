const { exec } = require("child_process");

function getUser(req) {
  const id = req.query.id;
  const query = "SELECT * FROM users WHERE id=" + id; // SQL injection
  console.log(query);
}

function run(cmd) {
  exec(cmd); // command injection
}

module.exports = { getUser, run };
