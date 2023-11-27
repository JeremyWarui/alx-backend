import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient({ host: "127.0.0.1", port: 6379 });
const getAsync = promisify(client.get).bind(client);

try {
  client.on('connect', () =>
    console.log(`Redis client connected to the server`)
  );
} catch (err) {
  console.error(`Redis client not connected to the server: ${err}`);
}

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const val = await getAsync(schoolName);
  console.log(val);
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
