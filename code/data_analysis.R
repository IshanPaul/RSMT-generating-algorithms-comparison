library("ggplot2")

df = read.csv(file = "/Users/ishanpl/Desktop/stats607/unit1/RSMT-generating-algorithms-comparison/datasets/summary.csv")
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
ggsave("/Users/ishanpl/Desktop/stats607/unit1/RSMT-generating-algorithms-comparison/plots/myplot.png", plot = p1, width = 6, height = 4, dpi = 300)

# Cockayne
m_cockayne <- lm(cockayne_time ~ as.factor(num_points) + grid_size + cockayne_steiner, data = df)
summary(m_cockayne)

# Geosteiner
m_geo <- lm(geosteiner_time ~ as.factor(num_points) + grid_size + geosteiner_steiner, data = df)
summary(m_geo)

# Flute
m_flute <- lm(flute_time ~ as.factor(num_points) + grid_size + flute_steiner, data = df)
summary(m_flute)



