from aiosmtpd.controller import Controller


class CustomHandler:
    async def handle_DATA(self, server, session, envelope):
        print("Message from:", envelope.mail_from)
        print("Message to:", envelope.rcpt_tos)
        print("Message data:", envelope.content.decode("utf8", errors="replace"))
        print("End of message")
        return "250 OK"


if __name__ == "__main__":
    controller = Controller(CustomHandler(), hostname="localhost", port=1025)
    controller.start()

    # Keep the script running to handle incoming SMTP connections
    print("SMTP server running on localhost:1025. Press Ctrl+C to stop.")
    try:
        import asyncio

        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        print("Shutting down SMTP server...")
        controller.stop()
