from prefect import serve

from flows.hello import hello

def generate_deployment(name):
    return hello.to_deployment(
        name=name,
        parameters={"name": name},
        tags=["serve"],
    )

if __name__ == "__main__":
    serve(
        generate_deployment("marvin"),
        generate_deployment("arthur"),
        generate_deployment("trillian"),
        query_seconds=5,
        limit=5,
    )
