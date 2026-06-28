async function getResponse(is_tea) {
  try {
    const url = `/api/response?is_tea=${Boolean(is_tea)}`;
    const response = await fetch(url);

    const data = await response.json();

    const response_section = document.getElementById("response_section");
    const status_code = document.getElementById("status_code");
    const response_element = document.getElementById("response");

    const raw_resp = document.getElementById("raw_resp");
    const raw_section = document.getElementById("raw_section");

    raw_section.style.display = "block";
    response_section.style.display = "flex";

    raw_resp.style.display = "flex";

    status_code.innerText = response.status;
    status_code.href = url;

    response_element.innerText = data.response;

    raw_resp.innerText = JSON.stringify(data, null, 2);
  } catch (error) {
    console.log("Error fetching data:", error);
  }
}
