import redis from 'redis';

const client = redis.createClient({ host: '127.0.0.1', port: 6379 });

try {
  client.on('connect', () =>
    console.log(`Redis client connected to the server`)
  );
} catch (err) {
  console.error(`Redis client not connected to the server: ${err}`);
}

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
