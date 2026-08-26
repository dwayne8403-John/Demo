<!DOCTYPE html>
<html lang="ta">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Birthday Wish</title>
<style>
  body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #1e272e;
    color: white;
    text-align: center;
    margin: 0;
  }
  .container {
    max-width: 400px;
    padding: 30px;
    background: #2f3640;
    border-radius: 15px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.3);
  }
  .hidden {
    display: none;
  }
  button {
    background-color: #ff4757;
    color: white;
    border: none;
    padding: 12px 25px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 8px;
    cursor: pointer;
    margin-top: 20px;
    transition: background 0.3s;
  }
  button:hover {
    background-color: #ff6b81;
  }
  /* Step 2 Animation */
  .gift-animation {
    font-size: 60px;
    animation: bounce 1s infinite alternate;
  }
  @keyframes bounce {
    from { transform: translateY(0); }
    to { transform: translateY(-20px); }
  }
  /* Step 3 Text Animation */
  .animated-text {
    font-size: 28px;
    font-weight: bold;
    color: #ffa502;
    text-shadow: 2px 2px 5px rgba(255, 165, 2, 0.5);
    animation: zoomInOut 1.5s ease-in-out infinite alternate;
  }
  @keyframes zoomInOut {
    from { transform: scale(0.9); }
    to { transform: scale(1.1); }
  }
</style>
</head>
<body>

<div class="container">
  <!-- முதல் பக்கம் -->
  <div id="step1">
    <h2> Hii Machaa... unakku oru chinna surprise ! 🎉</h2>
    <button onclick="showStep('step2')">Next</button>
  </div>

  <!-- இரண்டாவது பக்கம் (அனிமேஷன் + பட்டன்) -->
  <div id="step2" class="hidden">
    <div class="gift-animation">🎁🎈🎊</div>
    <p style="margin-top: 20px; font-size: 18px;">உனக்காக ஒரு சின்ன சர்ப்ரைஸ்...</p>
    <button onclick="showStep('step3')">Next</button>
  </div>

  <!-- மூன்றாவது பக்கம் (டெக்ஸ்ட் அனிமேஷன்) -->
  <div id="step3" class="hidden">
    <h1 class="animated-text">இனிய பிறந்தநாள் வாழ்த்துக்கள்! 🎂✨</h1>
  </div>
</div>

<script>
  function showStep(stepId) {
    // அனைத்துப் பக்கங்களையும் மறைக்க
    document.getElementById('step1').classList.add('hidden');
    document.getElementById('step2').classList.add('hidden');
    document.getElementById('step3').classList.add('hidden');
    
    // குறிப்பிட்ட பக்கத்தை மட்டும் காட்ட
    document.getElementById(stepId).classList.remove('hidden');
  }
</script>

</body>
</html>
