import {modalState} from "../modalState.js";
import {API} from "../../services/api.js";

export async function initialiseDataTable(tableId, apiEndpoint) {
    const tableConfigs = await API.getTableConfig();

    // Add validation to check if config exists for the endpoint
    if (!tableConfigs[apiEndpoint]) {
        console.error(`No table configuration found for endpoint: ${apiEndpoint}`);
        return;
    }

    // Add table headers dynamically before initialization
    const headerRow = $('<tr>');
    tableConfigs[apiEndpoint].forEach(config => {
        headerRow.append($('<th>').text(config.data));
    });

    $(`#${tableId}`).find('thead').empty().append(headerRow);

    // Clear existing table instance
    if ($.fn.DataTable.isDataTable(`#${tableId}`)) {
        $(`#${tableId}`).DataTable().clear().destroy();
    }

    const table = $(`#${tableId}`).DataTable({
        processing: false,
        serverSide: false,
        select: true,
        dom: 'Bfrtip',
        buttons: [
            {
                text: 'Edit',
                action: function () {
                    const selectedData = table.row('.selected').data();
                    if (selectedData) {
                        modalState.openEditModal(tableId, selectedData);
                    }
                },
                enabled: false
            }
        ],
        ajax: {
            url: `${API.baseUrl}/${apiEndpoint}`,
            dataSrc: ""
        },
        columns: tableConfigs[apiEndpoint],
        destroy: true,
        initComplete: function () {
            $('#loading-spinner').hide();
            $('#data').removeClass('datatable-hidden');
        }
    });

    return table;
}
