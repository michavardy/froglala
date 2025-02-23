


# Uvicorn
```bash
python311 -m uvicorn src.main:app --reload
sudo python311 -m uvicorn src.main:app --host 0.0.0.0 --port 80
```

# froglala.service
```bash
/etc/systemd/system/froglala.service
```

# systemctl commands
```bash
sudo systemctl daemon-reload
sudo systemctl enable froglala
sudo systemctl start froglala
```