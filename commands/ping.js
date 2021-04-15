// ping

module.exports = {
    name: 'ping',
    description: 'Get latency of connection',
    execute(message, args) {
        message.channel.send('Pong')
    }
}
