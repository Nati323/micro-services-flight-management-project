import uvicorn

if __name__ == "__main__":
    uvicorn.run("webapp.application:app", host="127.0.0.1", port=8085, log_level="info")
