const events_db = [];
const fs = require ('fs')


const getEvents = (ctx) => {
  ctx.body = fs.readFileSync("../../01-web/tasks/#005/task005.html", "utf8");
  ctx.status = 200;
};

const addEvent = (ctx) => {
  events_db.push(ctx.request.body);
  ctx.body = "Event Created!";
  ctx.status = 201;
};

module.exports = {
  getEvents,
  addEvent
};