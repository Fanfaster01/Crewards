import os
from supabase import create_client, Client

url: str = "https://ollwqnmujknqabwbeuvt.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9sbHdxbm11amtucWFid2JldXZ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTY2MzcxMDUsImV4cCI6MjAxMjIxMzEwNX0.xvKTNkJ2ODiLo9HA9xN9lwunhQvdlwqCoJjugU5UrMQ"
supabase: Client = create_client(url, key)

