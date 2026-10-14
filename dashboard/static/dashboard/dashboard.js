document.addEventListener('DOMContentLoaded', () => {
  const data = window.dashboardData;
  const ctx = document.getElementById('performanceChart');
  new Chart(ctx, {type: 'line', data: {labels: ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May'], datasets: [{label: 'Team performance', data: [73, 76, 75, 81, 84, 88], borderColor: '#7257e8', backgroundColor: 'rgba(114,87,232,.09)', fill: true, tension: .42, pointBackgroundColor: '#7257e8', pointBorderColor: '#fff', pointBorderWidth: 2, pointRadius: 4}]}, options: {responsive:true, maintainAspectRatio:false, plugins:{legend:{display:false},tooltip:{backgroundColor:'#26223e',padding:10,displayColors:false}}, scales:{x:{grid:{display:false},border:{display:false},ticks:{color:'#999baa',font:{size:11}}},y:{min:50,max:100,ticks:{stepSize:10,color:'#999baa',font:{size:11}},grid:{color:'#f0eff5'},border:{display:false}}}}});
  new Chart(document.getElementById('goalsChart'), {type:'doughnut',data:{datasets:[{data:[82,18],backgroundColor:['#7257e8','#ebe8f8'],borderWidth:0,borderRadius:7}]},options:{cutout:'76%',responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{enabled:false}}}});
  const search = document.getElementById('employeeSearch');
  search.addEventListener('input', () => {const term = search.value.toLowerCase(); document.querySelectorAll('tbody tr').forEach(row => row.style.display = row.innerText.toLowerCase().includes(term) ? '' : 'none');});
});
