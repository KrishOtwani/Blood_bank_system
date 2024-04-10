// donate.js

document.addEventListener("DOMContentLoaded", function() {
    // Donation form submission handler
    document.getElementById('donate-form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the selected blood group and number of units donated
        const bloodGroup = document.getElementById('blood-group').value;
        const units = parseInt(document.getElementById('units').value);

        // Update the dashboard with the donated blood
        updateDashboard(bloodGroup, units);

        // Clear the form fields
        document.getElementById('blood-group').value = 'A'; // Reset to default
        document.getElementById('units').value = '';
    });
});

// Function to update the dashboard with donated blood
function updateDashboard(bloodGroup, units) {
    const bloodGroupElement = document.getElementById(`blood-group-${bloodGroup.toLowerCase()}`);
    let currentUnits = parseInt(bloodGroupElement.textContent);
    currentUnits += units;
    bloodGroupElement.textContent = currentUnits;
}
