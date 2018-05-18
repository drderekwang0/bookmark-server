const URL = "/bookmarks";

async function main() {
  const response = await fetch(URL);
  let data = await response.json();
  data = data.data;

  const table = $("#data");
  for (let d of data) {
    table.append(`
      <tr data-id="${d.id}">
        <td><a href="${d.url}">${d.title}</a></td>
        <td>
          <a class="read-button"><i class="fas fa-check"></i></a>
          <a class="delete-button"><i class="fas fa-trash"></i></a>
        </td>
      </tr>
    `);
  }

  $(".read-button").click(function(e) {
    const id = getCurrentID(e);
    requestBookmarkAction(id, "read");
    getCurrentRow(e).remove();
  });

  $(".delete-button").click(function(e) {
    const id = getCurrentID(e);
    requestBookmarkAction(id, "delete");
    getCurrentRow(e).remove();
  });
}

function getCurrentRow(e) {
  return $(e.currentTarget).parents("tr");
}

function getCurrentID(e) {
  return getCurrentRow(e).data("id");
}

async function requestBookmarkAction(id, action) {
  const url = `${URL}/${id}/actions/${action}`;
  const response = await fetch(url);
}

main();
