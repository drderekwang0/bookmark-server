async function main() {
  const url = "/bookmarks/";

  const response = await fetch(url);
  let data = await response.json();
  data = data.data;

  const table = $("#data");
  for (let d of data) {
    table.append(`
      <tr>
        <td><a href="${d.url}">${d.title}</a></td>
        <td></td>
      </tr>
    `);
  }
}

main();
