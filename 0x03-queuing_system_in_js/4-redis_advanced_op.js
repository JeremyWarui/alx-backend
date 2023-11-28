import redis from 'redis';

const client = redis.createClient({host: '127.0.0.1', port: 6379});

client.on('connect', () => console.log('Redis client connected to the server'));

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

const data = Object.entries({
  'Portland': 50,
  'Seattle': 80,
  'New York': 20,
  'Bogota': 20,
  'Cali': 40,
  'Paris': 2
});

for (let [key, value] of data) {
  client.hset('HolbertonSchool', key, value, redis.print);
};

client.hgetall('HolbertonSchool', (err, reply) => console.log(reply));
