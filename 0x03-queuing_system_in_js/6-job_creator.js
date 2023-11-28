import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '0720-798-0114',
  message: 'Hello, this is the code to verify your account',
}

const job = queue.create('push_notification_code', jobData).save();

job.on('enqueue', (id) => console.log(`Notification job created: ${id}`));

job.on('complete', () => console.log('Notification job completed'));

job.on('failed', () => console.log('Notification job failed'));
