import numpy as np

# =====================================================
# 1️⃣ Data Cleaning Example (Missing Values Handling)
# Real world use: Sales, Medical, User datasets
# =====================================================

# Dataset with missing value (np.nan means missing data)

data = np.array([10, 20, np.nan, 40, 50])

# Replace missing values with mean value

mean_value = np.nanmean(data)
data[np.isnan(data)] = mean_value

print("Cleaned Data:", data)


# =====================================================
# 2️⃣ Image Processing Example (Brightness Increase)
# Real world use: Face recognition, medical imaging

image = np.array([
    [100,120,130],
    [90,110,140],
    [80,100,120]
])

# Increase brightness

bright_image = image + 20

print("\nBright Image:")
print(bright_image)


# =====================================================
# 3️⃣ Machine Learning Calculation (Dot Product)
# Real world use: Regression, Neural Networks

weights = np.array([0.5, 1.2])
features = np.array([10, 20])

prediction = np.dot(weights, features)

print("\nML Prediction Example:", prediction)


# =====================================================
# 4️⃣ Data Analysis Example
# Real world use: Business analytics, finance

sales = np.array([200, 300, 250, 400, 350])

print("\nAverage Sales:", np.mean(sales))
print("Maximum Sales:", np.max(sales))


# =====================================================
# 5️⃣ Recommendation System Example
# Real world use: Netflix, Amazon, Spotify

user_preferences = np.array([5, 3, 0])
movie_features = np.array([0.8, 0.6, 0.4])

score = np.dot(user_preferences, movie_features)

print("\nRecommendation Score:", score)


# =====================================================
# 6️⃣ Simulation Example (Random Data Generation)
# Real world use: Stock market, risk simulation

stock_prices = np.random.normal(100, 10, 5)

print("\nSimulated Stock Prices:", stock_prices)


# =====================================================
# 7️⃣ Sensor Data Processing Example
# Real world use: IoT, weather monitoring

temperature = np.array([25, 26, 27, 29, 30])

print("\nAverage Temperature:", np.mean(temperature))


# =====================================================
# 8️⃣ Audio Signal Processing Example
# Real world use: Speech recognition, voice AI

audio_signal = np.array([0.2, 0.5, -0.3, 0.1])

amplified_signal = audio_signal * 2

print("\nAmplified Audio Signal:", amplified_signal)


# =====================================================
# 9️⃣ Scientific Computing Example
# Real world use: Physics simulation, research

x = np.linspace(0, 10, 5)
y = x ** 2

print("\nScientific Computing Example:")
print("X values:", x)
print("Y values:", y)


# =====================================================
# 🔟 Game Development Example (Movement Simulation)

position = np.array([5, 10])
velocity = np.array([1, 2])

new_position = position + velocity

print("\nGame Movement Simulation:", new_position)