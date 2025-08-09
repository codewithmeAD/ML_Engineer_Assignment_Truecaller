import pandas as pd
import numpy as np
from config import call_data_path, signup_data_path, message_data_path, search_data_path
breakpoint()
message_data = pd.read_csv(message_data_path, sep = '\t')
signup_data = pd.read_csv(signup_data_path, sep = '\t')
call_data = pd.read_csv(call_data_path, sep = '\t')
search_data = pd.read_csv(search_data_path, sep = '\t')


