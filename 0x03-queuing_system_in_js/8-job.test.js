import { expect } from 'chai';

import kue from 'kue';

import createPushNotificationsJobs from './8-job';

let queue;

const list = [
  {
    phoneNumber: '4153518780',
    message: 'Hello there'
  },
  {
    phoneNumber: '439572094294',
    message: 'Hello from this other side'
  }
];

describe('createPushNotificationsJobs', () => {
  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs(2, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should throw an error message if jobs is a string', () => {
    expect(() => createPushNotificationsJobs('Hello', queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should not display error message if jobs is an empty array', () => {
    expect(createPushNotificationsJobs([], queue)).to.equal(undefined);
  });

  it('should create a job for each user', function() {
    queue.createJob('push_notification_code_3', list[0]).save();
    queue.createJob('push_notification_code_3', list[1]).save();
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({phoneNumber: '4153518780', message: 'Hello there'});
  });
});
