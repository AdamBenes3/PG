const webSocket = require("ws");
module.exports = class Comunication{
    constructor(server){
        const wss = new webSocket.Server({
            server: server
        })
        this.wss = wss;
        this.wss.on("listening", () => {
            console.log("WSS online")
        })
        const clients = [];
        wss.on("connection", (ws, req) =>{
            clients.push(ws)
            ws.on("message", (msg) => {
                clients.forEach((el, index) => {
                    el.send(index+ ". posílá: " + msg);
                })
            })
        })
    }
};