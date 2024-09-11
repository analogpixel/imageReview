SERVICE_NAME = "view-wise.service"

install_service:
	@echo "Installing service..."
	@cp ./service/$(SERVICE_NAME) /etc/systemd/system/$(SERVICE_NAME)
	@systemctl daemon-reload
	@systemctl enable $(SERVICE_NAME)
	@systemctl start $(SERVICE_NAME)
	@echo "Service installed successfully."
