# -*- coding: utf-8 -*-
import os
from app.index import app

if __name__ == '__main__':
  app.run(host=os.getenv('APP_ADDRESS', 'localhost'), port=8000)
