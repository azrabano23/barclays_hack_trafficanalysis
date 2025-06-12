
# Load necessary libraries
library(ggplot2)
library(dplyr)
library(tidyr)

# Read the CSV file (make sure this is in your working directory)
df <- read.csv("traffic_accidents_3.csv", stringsAsFactors = FALSE)

# Convert injuries_fatal to numeric in case it's not
df$injuries_fatal <- as.numeric(df$injuries_fatal)

# Define the columns to analyze
cols <- c("weather_condition", "first_crash_type", "alignment", "intersection_related_i")

# Initialize an empty list to store plots
plot_list <- list()

# Loop over each column and create a bar plot
for (col in cols) {
  temp <- df %>%
    group_by(.data[[col]]) %>%
    summarise(injuries_fatal = sum(injuries_fatal, na.rm = TRUE)) %>%
    arrange(desc(injuries_fatal)) %>%
    slice_max(order_by = injuries_fatal, n = 15)  # Show top 15 to keep it readable

  p <- ggplot(temp, aes_string(x = col, y = "injuries_fatal")) +
    geom_bar(stat = "identity", fill = "skyblue", color = "black") +
    labs(
      title = paste("Fatal Injuries by", gsub("_", " ", col)),
      x = gsub("_", " ", col),
      y = "Total Fatal Injuries"
    ) +
    theme_minimal() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))

  plot_list[[col]] <- p
}

# Use patchwork to combine plots (optional, install if needed)
# install.packages("patchwork")
library(patchwork)

# Combine and display the 4 plots in a 2x2 layout
(plot_list[[1]] | plot_list[[2]]) / (plot_list[[3]] | plot_list[[4]])
