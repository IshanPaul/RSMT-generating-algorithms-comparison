library("ggplot2")

df = read.csv(file = "../datasets/summary.csv")
head(df)

# Build combined data frame
df2 <- data.frame(
  time = c(df$cockayne_time, df$flute_time, df$geosteiner_time),
  label = as.factor(c(
    rep("cockayne", nrow(df)),
    rep("flute", nrow(df)),
    rep("geosteiner", nrow(df))
  ))
)

# Plot distribution of times
p1 <- ggplot(df2, aes(x = label, y = time)) +
  geom_boxplot() +
  theme_minimal()
 
# Save plot
ggsave("../plots/myplot.png", plot = p1, width = 6, height = 4, dpi = 300)

# Cockayne
m_cockayne <- lm(cockayne_time ~ as.factor(num_points) + grid_size + cockayne_steiner + cockayne_wirelength, data = df)
summary(m_cockayne)

# Geosteiner
m_geo <- lm(geosteiner_time ~ as.factor(num_points) + grid_size + geosteiner_steiner + geosteiner_wirelength, data = df)
summary(m_geo)

# Flute
m_flute <- lm(flute_time ~ as.factor(num_points) + grid_size + flute_steiner + flute_wirelength, data = df)
summary(m_flute)

jpeg("../plots/all_diagnostics.jpg", width = 1800, height = 1200, res = 150)
par(mfrow = c(3, 4))  # 3 models × 4 plots
plot(m_cockayne, which = 1:4, main = "Cockayne")
plot(m_geo, which = 1:4, main = "Geosteiner")
plot(m_flute, which = 1:4, main = "Flute")
dev.off()

