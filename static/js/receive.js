// receive.js

document.addEventListener("DOMContentLoaded", function() {
    // Receiving form submission handler
    document.getElementById('receive-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the selected blood group and number of units received
        const bloodGroup = document.getElementById('blood-group').value;
        const units = parseInt(document.getElementById('units').value);

        // Update the dashboard with the received blood
        updateDashboard(bloodGroup, -units); // Use negative units to subtract from the dashboard

        // Clear the form fields
        document.getElementById('blood-group').value = 'A'; // Reset to default
        document.getElementById('units').value = '';
    });
});

// Function to update the dashboard with received blood
function updateDashboard(bloodGroup, units) {
    const bloodGroupElement = document.getElementById(`blood-group-${bloodGroup.toLowerCase()}`);
    let currentUnits = parseInt(bloodGroupElement.textContent);
    currentUnits += units;

    // Ensure that the blood units don't go below 0
    currentUnits = Math.max(currentUnits, 0);

    bloodGroupElement.textContent = currentUnits;
}
