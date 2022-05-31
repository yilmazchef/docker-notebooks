import json
import httpx
import asyncio
import streamlit as st

st.header("Streaming Postgres Inserts to Streamlit!")


async def main():
    client = httpx.AsyncClient()
    async with client.stream(
        "GET", "https://notes-api.gerardbentley.com/listen_notes", timeout=None
    ) as response:
        async for chunk in response.aiter_bytes():
            st.json(json.loads(chunk))


asyncio.run(main())
