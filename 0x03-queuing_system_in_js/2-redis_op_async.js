import redis from 'redis';
import { promisify } from 'util';


const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);


client.on('connect', () => {
	console.log(`Redis client connected to the server`);
});

function setNewSchool(schoolName, value) {
	client.set(schoolName, value, redis.print);
}

async function displaySchoolvalue(schoolName) {
	const value = getAsync(schoolName);
	console.log(value);
}

cliennt.on('error', err => {
	console.log(`Redis client not connected to the server: ${err}`);
});

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
