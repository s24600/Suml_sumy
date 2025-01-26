#!/bin/bash

exec python3 prepare_csv.py &
exec python3 -m streamlit run app.py --server.address=0.0.0.0 --server.port=8501

