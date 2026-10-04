import requests

def test_multiply(a,b):
            response = requests.post("http://127.0.0.1:3306/sundram/mcp/multiply", json={"a": a, "b": b})
            if response.status_code == 200:
                print("Mulitiplication mcp called successfully", response.json()["result"])
            else:
                print("Failed to call multiplication mcp")

if __name__ == "__main__":
        test_multiply(3,4)
