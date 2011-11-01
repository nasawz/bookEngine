//
//  RootViewController.h
//  TilingDemo
//
//  Created by zhe wang on 11-11-1.
//  Copyright (c) 2011年 __MyCompanyName__. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "TiledScrollView.h"
#import "TapDetectingView.h"

@interface RootViewController : UIViewController <TiledScrollViewDataSource,TapDetectingViewDelegate> {
    
    TiledScrollView *imageScrollView;
    NSString        *currentImageName;
}

@end
