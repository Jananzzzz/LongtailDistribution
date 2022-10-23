
            # print(y_predicted)
            # print(y_train)
            # print(y_predicted.size(), y_predicted.dtype)
            # print(y_train.size(), y_train.dtype)
            # assert 1 == 2
            sampling_strategy = {0:4, 1:3, 2:5, 3:6, 4:5, 5:4, 6:5}
            rus = RandomUnderSampler(sampling_strategy=sampling_strategy)
            y_predicted = y_predicted.cpu()
            y_train = y_train.cpu()
            
            status = 0
            try:
                y_predicted, y_train = rus.fit_resample(y_predicted.detach().numpy(), y_train.detach().numpy())
            except:
                status = 1
            if status == 1:
                continue
            
            # print(y_predicted)                                      
            # print(y_train)
            # print(y_predicted.size(), y_predicted.dtype)
            # print(y_train.size(), y_train.dtype)
            # assert 1 == 2

            y_predicted = torch.from_numpy(y_predicted)

            for i in range(2):
                y_predicted = torch.cat((y_predicted, y_predicted), 0)
                y_train = np.append(y_train, y_train)
                
            y_train = torch.from_numpy(y_train)

            print(y_predicted) # test
            print(y_train) #test
            print(y_predicted.size()) # test
            print(y_train.size()) # test