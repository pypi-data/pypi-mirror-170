var data=[['c1', 'c2'], [1, 2]];
/**
 * @param  {} pg_no
 * @param  {} table_id
 */
function set_active_page(pg_no, table_id) {
    // get number of pages.
    const n_pages = document.getElementById(table_id).tBodies.length;
    for (let i = 0; i < n_pages; i++) {
        const table_ele = document.getElementById(table_id + '-p' + i);
        if (i == pg_no) {
            // make this page visible.
            table_ele.removeAttribute('display');
            class_name = 'active';
        }
        else {
            // make this page invisible.
            table_ele.style.display = 'none';
            class_name = '';
        }
        // configure page button if table has multiple pages.
        const pg_btn_ele = document.getElementById(table_id + '-b' + i);
        if (pg_btn_ele) {
            pg_btn_ele.className = class_name;
        }
    }
}

function set_page_buttons(pg_cnt, table_id) {
    const pg_btns_ele = document.getElementById(table_id + '-pages');
    // get current number of pages.
    const current_pg_cnt = pg_btns_ele.childElementCount;
    // check if pages should be added or removed.
    let pages_to_add = pg_cnt - current_pg_cnt;
    if (pages_to_add > 0) {
        const links_ele = document.createDocumentFragment();
        for (let i = current_pg_cnt; i < pg_cnt; i++) {
            a = document.createElement('a');
            a.id = table_id + '-b' + i;
            a.onclick = function () { set_active_page(i, table_id); };
            a.text = i + 1;
            a.href = '#';
            links_ele.appendChild(a);
        }
        pg_btns_ele.appendChild(links_ele);
    }
    else if (pages_to_add < 0) {
        // currently too many pages, so remove some.
        while (pages_to_add++ < 0) {
            pg_btns_ele.removeChild(pg_btns_ele.lastElementChild);
        }
    }
}

function add_table_row(tbody_ele, row_data, row_id) {
    const row_ele = tbody_ele.insertRow();
    row_ele.id = row_id;
    const n_cells = row_data.length;
    for (let i = 0; i < n_cells; i++) {
        const cell_ele = row_ele.insertCell();
        cell_ele.id = row_id + '-c' + i;
        cell_ele.appendChild(document.createTextNode(row_data[i]));
    }
}

function add_table_page(table_ele, rows, pg_no) {
    // add this page's tbody to table.
    const tbody_ele = document.createElement('tbody');
    const page_id = table_ele.id + '-p' + pg_no;
    tbody_ele.id = page_id;
    if (pg_no != 0) {
        tbody_ele.style.display = 'none';
    }
    table_ele.appendChild(tbody_ele);
    // insert rows into tbody.
    console.log("Loading page " + pg_no + " rows: " + rows)
    const n_rows = rows.length;
    for (let i = 0; i < n_rows; i++) {
        add_table_row(tbody_ele, rows[i], page_id + '-r' + i);
    }
}

function load_table(rows, rows_per_page, table_id) {
    const table_ele = document.getElementById(table_id);
    // clear any existing table.
    while (table_ele.firstChild) {
        table_ele.removeChild(table_ele.firstChild);
    }
    // load table header.
    const thead_ele = document.createElement('thead');
    table_ele.appendChild(thead_ele);
    const header_ele = thead_ele.insertRow();
    // first row should be header and the rest should be data.
    const header = rows.shift();
    console.log("Loading header: ", header)
    for (let col_name of header) {
        header_ele.insertCell().appendChild(document.createTextNode(col_name));
    }
    // load table body.
    if (rows_per_page) {
        // create a multi-page table.
        // calculate the number paginated table bodies that are needed.
        const pg_cnt = Math.ceil(rows.length / rows_per_page);
        // load data for each page.
        for (let i = 0; i < pg_cnt; ++i) {
            add_table_page(table_ele, rows.splice(0, rows_per_page), i);
        }
        // create page buttons.
        set_page_buttons(pg_cnt, table_id);
        set_active_page(0, table_id);
    }
    else {
        console.log("Loading single page table.")
        // put all rows on a single page.
        add_table_page(table_ele, rows, 0);
    }
}

function update_table(table_id, data) {
    const tbody_ele = document.getElementById(table_id);
    for (const [page_num, row_col_data] of Object.entries(data)) {
        const page_id = table_id + '-p' + page_num;
        for (const [row_num, col_data] of Object.entries(row_col_data)) {
            const row_id = page_id + '-r' + row_num;
            if (document.getElementById(row_id) === null) {
                add_table_row(tbody_ele, row_data, row_id);
            }
            else {
                for (const [cell_num, cell_data] of Object.entries(col_data)) {
                    const cell_ele = document.getElementById(row_id + '-c' + cell_num);
                    cell_ele.innerText = cell_data;
                }
            }
        }
    }
}

function stream_table_updates(table_id, ws_endpoint) {
    // ws_endpoint format: 'ws://localhost:8000/ws'
    const ws = new WebSocket(ws_endpoint);
    ws.onmessage = function (event) {
        update_table(table_id, JSON.parse(event.data));
    };
}