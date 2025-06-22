var API_BASE = "http://localhost:5002"; // need to change for prod

export async function getData(path){
    const result = await fetch(`${API_BASE}${path}`);
    if (!result.ok) {
        throw new Error(`GET ${path} failed`);
    }
    return result.json();
}