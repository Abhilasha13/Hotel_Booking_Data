library(C50)

hotel_bookings_data <- read.csv('/Users/ashutoshshanker/Desktop/Dataset_BI_Project/hotel_bookings_dataset.csv', na.strings=' NA')
summary(hotel_bookings_data)
sample_size = floor(0.8 * nrow(hotel_bookings_data))
training_adult = sample(nrow(hotel_bookings_data), size = sample_size)
train <- hotel_bookings_data[training_adult,]
test <- hotel_bookings_data[-training_adult,]

predictors <- c('lead_time', 'arrival_date_month','total_of_special_requests', 'required_car_parking_spaces', 		'booking_changes','market_segment','previous_cancellations','adr','deposit_type','arrival_date_week_number')
train$is_canceled = as.factor(train$is_canceled)
str(train$is_canceled)
model <- C5.0.default(x = train[,predictors], y = train$is_canceled)
summary(model)

random_hotel_booking_pred <- predict(model, newdata = test)
hotel_booking_evaluation <- cbind(test, random_hotel_booking_pred)
head(hotel_booking_evaluation)

hotel_booking_evaluation$correct <- ifelse(hotel_booking_evaluation$is_canceled == hotel_booking_evaluation$random_hotel_booking_pred,1,0)
sum(hotel_booking_evaluation$correct)/nrow(hotel_booking_evaluation)
