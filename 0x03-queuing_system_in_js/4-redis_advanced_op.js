import redis from 'redis';

const client = redis.createClient();

client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
	console.log(`Redis client connected to server`);;
});

const KEY = "HolbertonSchools";

const cities = ['Portland', 'Seattle', 'New York', 'Bogota', 'Cali', 'Paris'];

const numbers = [50, 80, 20, 20, 40, 2];

cities.forEach((city, index) => {
	client.hset(KEY, city, numbers[index], redis.print);
});

client.hgetall(KEY, (err, value) => {
	console.log(value);
});
