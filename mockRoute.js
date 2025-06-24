const helpService = require('./helpService');

function simulateRequest() {
  const userId = 1;
  const description = 'I need help with groceries';

  helpService.createRequest(userId, description);
}

simulateRequest();
