'use strict';

// Menu Node Context
class Slideshow extends Component {

    // Constructor
    constructor(componentIndex) {

        // Call parent constructor
        super(componentIndex);

        // Create DOM element
        let containerDiv = createElement("div", this.id.substring(1), "component-slideshow");

        // Create carousel
        let carouselDiv = createElement("div", this.id.substring(1) + "-carousel", "carousel slide");
        $(carouselDiv).css('display', 'flex');
        $(carouselDiv).css('flex-direction', 'column');
        $(carouselDiv).css('align-items', 'center');
        $(carouselDiv).css('justify-content', 'start');
        $(carouselDiv).css('width', '100%');
        $(carouselDiv).css('background-color', 'rgb(0,0,0,0.5)');
        $(carouselDiv).css('padding-left', '20px');
        $(carouselDiv).css('padding-right', '20px');
        $(carouselDiv).css('height', '100%');

        // Create carousel inner
        let carouselInnerDiv = createElement("div", this.id.substring(1) + "-carousel-inner", "carousel-inner");
        $(carouselInnerDiv).css('flex-grow', '1')

        // Create control prev
        let controlPrev = createElement("button", this.id.substring(1) + "-control-prev", "carousel-control-prev");
        $(controlPrev).attr("type", "button");
        $(controlPrev).attr("data-bs-target", "#" + this.id.substring(1) + "-carousel");
        $(controlPrev).attr("data-bs-slide", "prev");
        $(controlPrev).css("background-color", 'transparent !important');
        $(controlPrev).css("width", '20px');
        $(controlPrev).css("height", '20px');
        $(controlPrev).css("display", 'flex');
        $(controlPrev).css("position", 'relative');
        $(controlPrev).css("margin-left", '20px');
        $(controlPrev).css("margin-right", '20px');

        // Create control prev icon
        let controlPrevIcon = createElement("span", this.id.substring(1) + "-control-prev-icon", "carousel-control-prev-icon");
        $(controlPrevIcon).attr("aria-hidden", "true");

        // Create control prev text
        let controlPrevText = createElement("span", this.id.substring(1) + "-control-prev-text", "visually-hidden");
        controlPrevText.innerHTML = "Previous";

        // Create caoursel controls
        let carouselControls = createElement("div", this.id.substring(1) + "-carousel-controls", "");
        $(carouselControls).css('width', '100%');
        $(carouselControls).css('justify-content', 'space-evenly');
        $(carouselControls).css('display', 'flex');
        $(carouselControls).css('align-items', 'center');
        $(carouselControls).css('padding', '12px');

        // Create control next
        let controlNext = createElement("button", this.id.substring(1) + "-control-next", "carousel-control-next");
        $(controlNext).css("background-color", 'red !important');
        $(controlNext).css("width", '20px');
        $(controlNext).css("height", '20px');
        $(controlNext).css("display", 'flex');
        $(controlNext).css("position", 'relative');
        $(controlNext).css("margin-left", '20px');
        $(controlNext).css("margin-right", '20px');
        $(controlNext).attr("type", "button");
        $(controlNext).attr("data-bs-target", "#" + this.id.substring(1) + "-carousel");
        $(controlNext).attr("data-bs-slide", "next");

        // Create control next icon
        let controlNextIcon = createElement("span", this.id.substring(1) + "-control-next-icon", "carousel-control-next-icon");
        $(controlNextIcon).attr("aria-hidden", "true");

        // Create control next text
        let controlNextText = createElement("span", this.id.substring(1) + "-control-next-text", "visually-hidden");
        controlNextText.innerHTML = "Next";

        // Append elements
        controlPrev.appendChild(controlPrevIcon);
        controlPrev.appendChild(controlPrevText);
        controlNext.appendChild(controlNextIcon);
        controlNext.appendChild(controlNextText);
        carouselDiv.appendChild(carouselInnerDiv);
        carouselControls.appendChild(controlPrev);
        carouselControls.appendChild(controlNext);
        carouselDiv.appendChild(carouselControls);
        containerDiv.appendChild(carouselDiv);

        qs("#artemis-builder").appendChild(containerDiv);        
        
        // Setup size
        $(this.id).css("width", '100%');
        $(this.id).css("height", '100%');

        // Set constraints
        super.minWidth = 1 * 8;
        super.minHeight = 1 * 8;

        // Setup click callback
        super.setupClickCallback();
    }

    // Add editable content
    addEditableContent() {

       
    }

    // Get state
    getState() {
        let state = super.getState();
        return state;
    }

    // Load state
    loadState(state) {

        // Clear carousel
        let carouselInner = qs(this.id + "-carousel-inner");
        while (carouselInner.firstChild) {
            carouselInner.removeChild(carouselInner.firstChild);
        }

        // Load state
        state.image_paths.forEach(element => {

            
            // create carousel item
            let carouselItem = createElement("div", "", "carousel-item");
            $(carouselItem).css('padding-top', '0px');
            $(carouselItem).css('max-height', '100%');
            $(carouselItem).css('height', '100%');

            // carousel wrapper
            let carouselWrapper = createElement("div", "", "");
            $(carouselWrapper).css('display', 'flex');
            $(carouselWrapper).css('flex-direction', 'column');
            $(carouselWrapper).css('align-items', 'center');
            $(carouselWrapper).css('justify-content', 'start');
            $(carouselWrapper).css('height', '100%');
            $(carouselWrapper).css('max-height', '100%');

            // Create carousel header
            let carouselHeaderDiv = createElement("div", this.id.substring(1) + "-carousel-header", "carousel-header");
            $(carouselHeaderDiv).css('display', 'flex');
            $(carouselHeaderDiv).css('flex-direction', 'column');
            $(carouselHeaderDiv).css('align-items', 'center');
            $(carouselHeaderDiv).css('width', '100%');
            $(carouselHeaderDiv).css('background-color', 'transparent');
            $(carouselHeaderDiv).css('padding-top', '10px');
            $(carouselHeaderDiv).css('padding-bottom', '5px');

            let carouselHeaderText = createElement("h4", this.id.substring(1) + "-carousel-header-text", "");
            $(carouselHeaderText).text(element['title']);
            $(carouselHeaderText).css('color', 'white');
            $(carouselHeaderText).css('margin-left', '10px');
            $(carouselHeaderText).css('margin-right', '10px');

            let carouselHeaderDescription = createElement("p", this.id.substring(1) + "-carousel-header-description", "");
            $(carouselHeaderDescription).text(element['description']);
            $(carouselHeaderDescription).css('color', 'white');
            $(carouselHeaderDescription).css('margin-left', '10px');
            $(carouselHeaderDescription).css('margin-right', '10px');
            $(carouselHeaderDescription).css('margin-bottom', '5px');

            carouselHeaderDiv.appendChild(carouselHeaderText);
            carouselHeaderDiv.appendChild(carouselHeaderDescription);
            $(carouselWrapper).append(carouselHeaderDiv);


            // create carousel image
            let carouselImageDiv = createElement("div", "", "carousel-image");
            $(carouselImageDiv).css('width', '100%');
            $(carouselImageDiv).css('height', '100%');
            $(carouselImageDiv).css('min-height', '0px');
            $(carouselImageDiv).css('padding-top', '0px');
            $(carouselImageDiv).css('flex-grow', '1');
            $(carouselWrapper).append(carouselImageDiv);

            let carouselImage = createElement("img", "", "d-block w-100");
            $(carouselImage).attr("src", element['path']);
            $(carouselImage).attr("alt", "Slide");
            $(carouselImage).css("margin-top", "0px");
            $(carouselImage).css("margin-bottom", "0px");
            $(carouselImage).css("object-fit", "contain");
            $(carouselImage).css("max-height", "100%");
            carouselImageDiv.appendChild(carouselImage);

            // append elements
            $(carouselItem).append(carouselWrapper);
            $(this.id + "-carousel-inner").append(carouselItem);
        });

        // set first item to active
        $(this.id + "-carousel-inner").children().first().addClass("active");
    }
}
